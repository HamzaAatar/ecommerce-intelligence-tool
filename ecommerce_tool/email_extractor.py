import requests
import logging
from config import Config


class EmailExtractor:
    """Extract and validate email contacts"""

    BASE_URL = "https://api.hunter.io/v2/domain-search"

    @classmethod
    def extract_emails(cls, websites):
        """
        Extract verified emails for given websites

        Args:
            websites (list): List of website domains

        Returns:
            dict: Email verification results
        """
        logger = logging.getLogger(__name__)
        email_data = {}

        for website in websites:
            try:
                domain = website.split("//")[-1].split("www.")[-1]

                params = {"domain": domain, "api_key": Config.HUNTERIO_API_KEY}

                response = requests.get(cls.BASE_URL, params=params)
                data = response.json()

                emails = data.get("data", {}).get("emails", [])
                verified_email = emails[0]["value"] if emails else ""

                email_data[website] = {
                    "Verified Email": "Yes" if verified_email else "No",
                    "Email": verified_email,
                }

            except Exception as e:
                logger.warning(f"Email extraction failed for {website}: {e}")
                email_data[website] = {"Verified Email": "No", "Email": ""}

        return email_data
