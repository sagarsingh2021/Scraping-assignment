import logging
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from mba_app.models import University

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Fetches university data from topmba.com and saves it to the database'

    def handle(self, *args, **options):

        # Initialize the Chrome driver
        driver = webdriver.Chrome()

        # Navigate to the website
        driver.get('https://www.topmba.com/colleges')
        driver = webdriver.Chrome()

        driver.get('https://www.topmba.com/colleges')


        wait = WebDriverWait(driver, 10)
        div = wait.until(EC.visibility_of_element_located((By.ID, 'univListingCards')))


        university_list = div.find_elements(By.CLASS_NAME, 'card')

        # Loop through the div elements and extract the data
        for div in university_list:

            uni_det = div.find_element(By.CLASS_NAME, 'uni-det')
            anchor_tag = uni_det.find_element(By.TAG_NAME, 'a')

            ranking = (div.find_element(By.CLASS_NAME, 'uni_ranking')).find_element(By.CLASS_NAME, 'cont').text

            has_scholarship = 'No'
            try:
                scholarship = (div.find_element(By.XPATH, './/li[@title="Scholarships"]/span[2]'))

                if scholarship.get_attribute('title') == 'Yes':
                    has_scholarship = 'Yes'
                print(has_scholarship)
            except (NoSuchElementException, TimeoutException) as error:
                logger.exception(f'Error while fetching scholarship: {error}')

            location = uni_det.find_element(By.CLASS_NAME, 'location')
            name = anchor_tag.get_attribute('title')
            website_url = anchor_tag.get_attribute('href')

            # Check if the university already exists in the database
            university = University.objects.filter(name=name).first()

            if university is None:
                university = University(name=name, scholarship=has_scholarship, website_url=website_url, location=location.text, rank=ranking)
                university.save()

        # Close the driver
        driver.quit()
