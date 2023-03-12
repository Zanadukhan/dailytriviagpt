import replicate

class ImgGen:
    def __init__(self, prompt):
        model = replicate.models.get("stability-ai/stable-diffusion")
        version = model.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")
        self.inputs = {
            'prompt': prompt,
            'image_dimensions': "768x768",
            'num_outputs': 1,
            'num_inference_steps': 50,
            'guidance_scale': 7.5,
            'scheduler': "DPMSolverMultistep",
        }
        self.output = version.predict(**self.inputs)