# Warning control
import warnings
warnings.filterwarnings('ignore')

from blog_writer.crew import BlogWriter
from blog_writer.get_image import get_image

def run():
    """
    Run the crew.
    """

    topic = "Introduction to Machine Learning: Difference between Supervised and Unsupervised Learning"

    # Initialize the crew
    my_writer = BlogWriter()

    # Run
    result = (my_writer
              .crew()
              .kickoff(inputs = {
                  'topic': topic
                  })
    )

    # Get the image
    get_image()