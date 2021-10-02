from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
import os

# https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries

def run_report(property_id):
    # stupid, but the docs are crap
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tweet-a-term-stats-d8b4ef62a65c.json"

    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="active28DayUsers")],
        date_ranges=[DateRange(start_date="2021-01-01", end_date="today")],
    )
    response = client.run_report(request)

    return response

if __name__ == '__main__':
    from secrets import property_id
    run_report(property_id)
