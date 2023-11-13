import logging
from zut import JSONApiClient
from .choices import ReportAction, ReportOrigin

logger = logging.getLogger(__name__)


class CMDBaseApiClient(JSONApiClient):
    force_trailing_slash = True
    
    def __init__(self, base_url: str, api_token: str):
        super().__init__()
        self.base_url = base_url
        self.api_token = api_token
    

    def get_request_headers(self, url: str):
        headers = super().get_request_headers(url)
        headers['Authorization'] = f"Token {self.api_token}"
        return headers
    

    def report(self, data: dict|list[dict]):
        # Post data
        results = self.post('/report', data)

        # Analyze results
        reports = results.pop('reports')
        results.pop('by')
        by_username = results.pop('by_username')
        origin = ReportOrigin(results.pop('origin'))
        root_items = results.pop('root_items')
        issue_details = results.pop('issue_details')

        for i in range(0, len(data) if isinstance(data, list) else 1):
            prefix = f"index {i}: " if isinstance(data, list) else ''

            if logger.isEnabledFor(logging.DEBUG):
                root_item = root_items[i]
                if root_item and logger.isEnabledFor(logging.DEBUG):
                    logger.debug(f"{prefix}posted root item {root_item['fullname']} [{ReportAction(root_item['action']).label}]")

            issue = issue_details[i]
            if issue:
                logger.warning(f"{prefix}{', '.join(issue) if isinstance(issue, list) else issue}")

        logger.log(logging.WARNING if results['issues'] else logging.INFO, f"handled {origin.label} reports by {by_username}: {reports}, {', '.join(f'{k}: {v}' for k, v in results.items())}")
