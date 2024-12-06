from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging
import time

class AmazonValidator:
    """Validate brand presence on Amazon marketplace"""
    
    @classmethod
    def validate_amazon_presence(cls, brands):
        """
        Check if brands are selling on Amazon
        
        Args:
            brands (list): List of brand names to validate
        
        Returns:
            dict: Brand presence status
        """
        logger = logging.getLogger(__name__)
        
        # Configure Chrome options for headless browsing
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        
        amazon_presence = {}
        
        try:
            for brand in brands:
                try:
                    search_url = f"https://www.amazon.com/s?k={brand.replace(' ', '+')}"
                    driver.get(search_url)
                    time.sleep(2)  # Page load wait
                    
                    # Check for search results
                    results = driver.find_elements(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
                    amazon_presence[brand] = 'Yes' if results else 'No'
                    
                    time.sleep(1)  # Rate limiting
                
                except Exception as brand_error:
                    logger.warning(f"Amazon validation failed for {brand}: {brand_error}")
                    amazon_presence[brand] = 'Unknown'
        
        finally:
            driver.quit()
        
        return amazon_presence
