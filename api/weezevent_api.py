from api.core import CoreApi


class Api(CoreApi):
    EVENTS = '/events'
    DATES = '/dates'
    TICKETS = '/tickets'
    TICKET_STATS = '/ticket/:id/stats'
    PARTICIPANT_LIST = '/participant/list'
    PARTICIPANT_ANSWERS = '/participant/:id/answers'
    SCAN_SETTINGS = '/scan/settings'
    SCAN_USER = '/scan/user'
    EVENT_DETAILS = '/event/:id/details/'
    EVENT_SEARCH = '/event/search/'
    EVENT_CATEGORIES = '/event/categories/'

    def get_events(self, params={}):
        return self._request_get(self.EVENTS, params)

    def get_dates(self, params={}):
        return self._request_get(self.DATES, params)

    def get_tickets(self, params={}):
        return self._request_get(self.TICKETS, params)

    def get_ticket_stats(self, ticket_id, params={}):
        url = self.TICKET_STATS.replace(':id', str(ticket_id))
        return self._request_get(url, params)

    def get_participant_list(self, params={}):
        return self._request_get(self.PARTICIPANT_LIST, params)

    def get_participant_answers(self, participant_id):
        url = self.PARTICIPANT_ANSWERS.replace(':id', str(participant_id))
        return self._request_get(url)

    def get_scan_settings(self):
        return self._request_get(self.SCAN_SETTINGS)

    def post_scan_user(self, name_user):
        params = {'user': name_user}
        return self._request_post(self.SCAN_USER, params)

    def get_event_details(self, event_id):
        url = self.EVENT_DETAILS.replace(':id', str(event_id))
        return self._request_get(url)

    def get_event_search(self, params={}):
        return self._request_get(self.EVENT_SEARCH, params)

    def get_event_categories(self):
        return self._request_get(self.EVENT_CATEGORIES)
