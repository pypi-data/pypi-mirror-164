from functools import partial
from cv2 import multiply
from . import BaseExplainer
from .explanation import Explanation
from .utils import parse_explainer_args
from captum.attr import Saliency, IntegratedGradients, InputXGradient
import torch


class GradientExplainer(BaseExplainer):
    NAME = "Gradient"

    def __init__(self, model, tokenizer, multiply_by_inputs: bool = True):
        super().__init__(model, tokenizer)
        self.multiply_by_inputs = multiply_by_inputs

        if self.multiply_by_inputs:
            self.NAME += " (x Input)"

    def compute_feature_importance(
        self,
        text: str,
        target: int == 1,
        **explainer_args,
    ):
        init_args, call_args = parse_explainer_args(explainer_args)

        item = self._tokenize(text)
        input_len = item["attention_mask"].sum().item()

        def func(input_embeds):
            item.pop("input_ids")
            outputs = self.model(inputs_embeds=input_embeds, **item)
            scores = outputs.logits[0]
            return scores[target].unsqueeze(0)

        dl = (
            InputXGradient(func, **init_args)
            if self.multiply_by_inputs
            else Saliency(func, **init_args)
        )

        inputs = self.get_input_embeds(text)
        attr = dl.attribute(inputs, **call_args)
        attr = attr[0, :input_len, :].detach()

        # pool over hidden size
        attr = attr.sum(-1)

        output = Explanation(text, self.get_tokens(text), attr, self.NAME, target)
        # norm_attr = self._normalize_input_attributions(attr.detach())
        return output


class IntegratedGradientExplainer(BaseExplainer):
    NAME = "Integrated Gradient"

    def __init__(self, model, tokenizer, multiply_by_inputs: bool = True):
        super().__init__(model, tokenizer)
        self.multiply_by_inputs = multiply_by_inputs

        if self.multiply_by_inputs:
            self.NAME += " (x Input)"

    def _generate_baselines(self, input_len):
        ids = (
            [self.tokenizer.cls_token_id]
            + [self.tokenizer.pad_token_id] * (input_len - 2)
            + [self.tokenizer.sep_token_id]
        )
        embeddings = self._get_input_embeds_from_ids(torch.tensor(ids))
        return embeddings.unsqueeze(0)

    def compute_feature_importance(self, text, target, **explainer_args):
        init_args, call_args = parse_explainer_args(explainer_args)
        item = self._tokenize(text)
        input_len = item["attention_mask"].sum().item()

        def func(input_embeds):
            item.pop("input_ids")
            n_samples = input_embeds.shape[0]
            attention_mask = item["attention_mask"].expand(n_samples, -1, -1)

            #  TODO Improve here to introduce batched forward
            outputs = self.model(
                inputs_embeds=input_embeds, attention_mask=attention_mask
            )
            scores = outputs.logits[0]
            return scores[target].unsqueeze(0)

        dl = IntegratedGradients(
            func, multiply_by_inputs=self.multiply_by_inputs, **init_args
        )
        inputs = self.get_input_embeds(text)
        baselines = self._generate_baselines(input_len)

        attr = dl.attribute(inputs, baselines=baselines, **call_args)
        attr = attr[0, :input_len, :].detach()

        # pool over hidden size
        attr = attr.sum(-1)

        # norm_attr = self._normalize_input_attributions(attr.detach())
        output = Explanation(text, self.get_tokens(text), attr, self.NAME, target)
        return output
