

class ProdiaResponse:
    """
    Prodia API response(after waiting for result)

    Attributes:
        job_id: id of the job
        image_url: URL of generated image
        json: JSON response(raw)
    """
    def __init__(self, output: dict):
        self.job_id = output['job']
        self.image_url = output['imageUrl']
        self.json = output