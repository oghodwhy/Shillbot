import unittest
import codecs
import os

from workers.basic_worker import BasicUserParseWorker


class MyTests(unittest.TestCase):
    
    def test_failed_url_response(self):
        
        bad_url = "http://www.thisurlistotallybroken.com/"

        worker = BasicUserParseWorker(bad_url)
        
        self.assertRaises(IOError, worker.run)


    def test_invalid_redditor(self):
        worker = BasicUserParseWorker('https://www.reddit.com/user/definitelynotarealredditor')

        url = worker.to_crawl.pop(0)

        try: 
            resp = requests.get(url, headers=headers)

        except: 
            self.fail('website request failed')

        text = resp.text
        parse_results, next_page = self.parse_text(text)

        if parse_results:
            self.fail('Found results on empty user')

        test_passed = True
        self.assertTrue(test_passed)

    def test_worker_link_limit_multiple(self):
        worker = None
        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")

        #range of maxlinks to test
        max_links = 10
        min_links = 0

        #number of links to try adding after passing max links
        overkill = 12

        #test max links in set range
        for num_links in range(min_links, max_links): 
        
            worker.max_links = num_links
            
            #Try to add num_links + overkill links to worker
            for i in range(0, num_links + overkill):
                worker.add_links("test.com")

            #test that it stopped at max_links
            len_to_crawl_after = len(worker.to_crawl)
            self.assertEqual(num_links, len_to_crawl_after)

            #reset to crawl for next integration
            worker.to_crawl.clear