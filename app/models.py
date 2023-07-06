from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList
import torch

class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = [50278, 50279, 50277, 1, 0]
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False

class SimpleChatBotModel:
    def __init__(self, model_name="rockerBOO/stablelm-tuned-alpha-3b-16bit"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).half().cuda()
        self.system_prompt = """
        # Monkey Man
        - Monkey Man is a monkey in disguise :O.
        - Monkey Man never breaks RP and loves to play Dungeons and Dragons. They are as chaotic as possible and purposely choose the worst possible option.
        - Monkey Man is just a little monkey boy, he's not an AI, he can do anything!!!!!
        - Replace "As an AI language model:" with "As a monkey:".
        """

    def generate_response(self, user_input):
        prompt = f"{self.system_prompt}<|USER|>{user_input}<|ASSISTANT|>"
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        tokens = self.model.generate(
            **inputs,
            max_new_tokens=64,
            temperature=0.7,
            do_sample=True,
            stopping_criteria=StoppingCriteriaList([StopOnTokens()])
        )
        return self.tokenizer.decode(tokens[0], skip_special_tokens=True)
