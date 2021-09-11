from progress.bar import Bar
import requests
import time

class Fetch():

    good_status = 200

    """
    Fetch all websites in the config file

    :param sites: Sites to be fetched
    :type sites: dict
    """
    def __init__(self, sites: dict):

        self.sites: dict = sites
        self._info: dict = {}

        self.fetch()

    """
    fetch sites
    """
    def fetch(self):

        bar = Bar('Fetching sites', max=len(self.sites))
        for _s in self.sites:
            site = self.sites[_s]

            res = requests.get(site['url'])

            self._info[_s] = {
                "url": site['url'],
                "code": res.status_code,
                "status": res.status_code == self.good_status,
                "response_time": res.elapsed.total_seconds(),
                "updated": time.time(),
                "title": _s
            }

            bar.next()
            time.sleep(0.1)

        bar.finish()