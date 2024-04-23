class CustomerReview:
    ID = None
    headline = None
    review_text = None
    product_id = None

    def __init__(self, ID, headline, review_text, product_id):
        """
        Constructor
        :param ID: ID of a review
        :param headline: headline of a review
        :param review_text: text of a review
        :param product_id: ID of the product to which the review refers
        """
        self.ID = ID
        self.headline = headline
        self.review_text = review_text
        self.product_id = product_id
