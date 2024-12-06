import requests
import pandas as pd
from .config import Config
import logging

class BuiltWithExtractor:
    """Extract e-commerce website data from BuiltWith"""
    BASE_URL = 'https://api.builtwith.com/v21/api.json'
    
    @classmethod
    def extract_ecommerce_data(cls, limit=None):
        """
        Extract e-commerce website data from BuiltWith API
        
        Args:
            limit (int, optional): Limit number of websites to extract
        
        Returns:
            pd.DataFrame: Extracted website data
        """
        logger = logging.getLogger(__name__)
        
        params = {
            'key': Config.BUILTWITH_API_KEY,
            'taxonomy': 'eCommerce Product',
            'format': 'json'
        }
        
        try:
            response = requests.get(cls.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            websites = []
            for site in data.get('Results', [])[:limit or Config.MAX_WEBSITES]:
                websites.append({
                    'Website': site.get('Domain', ''),
                    'Location': site.get('Country', ''),
                    'Website Sales Revenue': site.get('RevenueEstimate', 'N/A'),
                    'Tech Spend': site.get('TechSpend', 'N/A'),
                    'Traffic': site.get('Traffic', 'N/A')
                })
            
            df = pd.DataFrame(websites)
            logger.info(f"Extracted {len(df)} websites from BuiltWith")
            return df
        
        except requests.RequestException as e:
            logger.error(f"BuiltWith data extraction failed: {e}")
            return pd.DataFrame()
