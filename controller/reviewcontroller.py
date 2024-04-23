from model.customerreview import CustomerReview


class ReviewController:
    all_reviews = []
    found_reviews = []

    def create_review(self, headline, review_text, product_id):
        """
        creates an object costumerreview from the input and appends it to all_reviews
        :param headline: headline of a review
        :param review_text: text of a review
        :param product_id: ID of the product to which the review refers
        """
        ID = len(self.all_reviews)
        new_review = CustomerReview(ID=ID, headline=headline, review_text=review_text, product_id=int(product_id))
        self.all_reviews.append(new_review)

    def initial_reviews(self):
        """
        creates the reviews when the flask script has been started
        """
        self.create_review(headline="Not the best quality",
                           review_text="I have used the trousers for 6 months and now they are already torn.",
                           product_id=1000)
        self.create_review(headline="Love it", review_text="The pullover is perfect for the cold days.",
                           product_id=1002)
        self.create_review(headline="Size is slightly smaller",
                           review_text="The size is smaller than regular, but I love the pullover so much that I signed up at the gym.",
                           product_id=1002)
        self.create_review(headline="Nice hat",
                           review_text="He does what it should do: keeps the sun out of your face.", product_id=1007)
        self.create_review(headline="Cool brand",
                           review_text="I love the brand so I had to have this jacket! Money is only paper ;)",
                           product_id=1009)

    def find_review(self, IDofproduct):
        """
        finds the reviews to the given product ID and appends them to found_reviews
        :param IDofproduct: id of the product to which the reviews should be found
        """
        for review in self.all_reviews:
            if review.product_id == int(IDofproduct):
                self.found_reviews.append(review)
                continue
            elif review.product_id != int(IDofproduct):
                continue
