import unittest
import tempfile
import time
import requests

from tests.context import yfinance as yf


class TestCookieCache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tempCacheDir = tempfile.TemporaryDirectory()
        yf.set_tz_cache_location(cls.tempCacheDir.name)

    @classmethod
    def tearDownClass(cls):
        yf.cache._CookieDBManager.close_db()
        cls.tempCacheDir.cleanup()

    def _create_cookie(self):
        s = requests.Session()
        expiry = int(time.time()) + 3600
        s.cookies.set('A3', 'val', domain='yahoo.com', path='/', expires=expiry)
        cookies = s.cookies._cookies
        return {'yahoo.com': cookies['yahoo.com']}

    def test_store_and_lookup(self):
        cookie_data = self._create_cookie()
        cache = yf.cache.get_cookie_cache()
        cache.store('curlCffi', cookie_data)
        res = cache.lookup('curlCffi')
        self.assertIsNotNone(res)
        self.assertIn('yahoo.com', res['cookie'])
        self.assertIn('A3', res['cookie']['yahoo.com']['/'])

    def test_migrate_from_pickle(self):
        cookie_data = self._create_cookie()
        cache = yf.cache.get_cookie_cache()
        cache.initialise()
        db = cache.get_db()
        pickled = yf.cache._pkl.dumps(cookie_data, yf.cache._pkl.HIGHEST_PROTOCOL)
        with db.atomic():
            yf.cache._CookieSchema.insert(strategy='legacy', cookie_bytes=pickled).execute()
        res = cache.lookup('legacy')
        self.assertIsNotNone(res)
        self.assertIn('yahoo.com', res['cookie'])
        # ensure re-read uses json
        row = yf.cache._CookieSchema.get(yf.cache._CookieSchema.strategy == 'legacy')
        self.assertIsInstance(row.cookie_bytes, (bytes, bytearray))
        # should decode as json without exception
        yf.cache._json.loads(row.cookie_bytes.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

