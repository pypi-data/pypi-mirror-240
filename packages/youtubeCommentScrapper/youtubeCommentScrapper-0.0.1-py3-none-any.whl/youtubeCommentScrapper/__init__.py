from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import emoji

class YoutubeCommentScrapper:
    def __init__(self,videoUrl,commentNo):
        self.video_url = videoUrl
        self.commentNo = commentNo
        self.element_wait_time = 20
        self.driver = self.__web_driver()
    def __web_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver 
    def __get_comment_data(self,c):
        
        c_text=c.find_elements(By.XPATH,'.//div[contains(@id,"body")]/div[contains(@id,"main")]/div[contains(@id,"comment-content")]/ytd-expander/div[contains(@id,"content")]/yt-formatted-string/*')
        text=""
        if len(c_text)==0:
            text = c.find_element(By.XPATH,'.//div[contains(@id,"body")]/div[contains(@id,"main")]/div[contains(@id,"comment-content")]/ytd-expander/div[contains(@id,"content")]/yt-formatted-string')
            text= text.get_attribute('innerHTML').strip(' \n')

        for e in c_text:
            if e.tag_name == "img":
                text+=emoji.demojize(e.get_attribute("alt")).strip(":") + " "

            else:
                text+=e.get_attribute('innerHTML').strip(' \n') + " "

        c_author_name=c.find_element(By.XPATH,'.//div[contains(@id,"body")]/div[contains(@id,"main")]/div[contains(@id,"header")]/div[contains(@id,"header-author")]/h3/a[contains(@id,"author-text")]/span')
        c_date=c.find_element(By.XPATH,'.//div[contains(@id,"body")]/div[contains(@id,"main")]/div[contains(@id,"header")]/div[contains(@id,"header-author")]/yt-formatted-string/a')
        c_likes=c.find_element(By.XPATH,'.//div[contains(@id,"body")]/div[contains(@id,"main")]/ytd-comment-action-buttons-renderer/div[contains(@id,"toolbar")]/span')

        return {"comment_author":c_author_name.get_attribute('innerHTML').strip(' \n'),
                "comment_date":c_date.get_attribute('textContent'),
                "comment_text":text,
                "comment_likes":c_likes.get_attribute('innerHTML').strip(' \n')}
    
    def __get_comment_replies(self,comment_no):


        replies_xpath = '''/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[{0}]/div[contains(@id,"replies")]'''.format(comment_no)
        replies = self.driver.find_element(By.XPATH,replies_xpath)
        if len(replies.find_elements(By.XPATH,"*")) == 0:
            return []

        expand_replies_button = replies.find_element(By.XPATH,'.//ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@class,"expander-header")]/div[contains(@class,"more-button")]')
        actions = ActionChains(self.driver)
        actions.move_to_element(expand_replies_button)

        actions.click().perform()

        #   expand_replies_button.click()
        timeout_seconds = 5

        # start the timer
        start_time = time.time()
        while True:
                if time.time() - start_time > timeout_seconds:
                    show_more_button = self.driver.find_elements(By.XPATH,replies_xpath+'/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/ytd-continuation-item-renderer')
                    if len(show_more_button) == 0:
                        show_more_button = None
                    break

        while( show_more_button!=None):


            self.driver.execute_script("arguments[0].scrollIntoView();", show_more_button[0])
            # self.driver.execute_script("window.scrollBy(0, -100);")



            More_button = WebDriverWait(self.driver, self.element_wait_time).until(EC.element_to_be_clickable((By.XPATH,'''/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[{0}]/div[contains(@id,"replies")]/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/ytd-continuation-item-renderer/div[contains(@id,"button")]/ytd-button-renderer/yt-button-shape/button'''.format(comment_no))))
            More_button = WebDriverWait(self.driver, self.element_wait_time).until(EC.visibility_of_element_located((By.XPATH,'''/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[{0}]/div[contains(@id,"replies")]/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/ytd-continuation-item-renderer/div[contains(@id,"button")]/ytd-button-renderer/yt-button-shape/button'''.format(comment_no))))

            if More_button.is_displayed():
                # More_button.click()
                actions = ActionChains(self.driver)
                actions.move_to_element(More_button)

                actions.click().perform()
                # self.driver.execute_script("arguments[0].click();", More_button)
            else:
                continue


            while True:
                spinner_loader = self.driver.find_elements(By.XPATH,'''/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[{0}]/div[contains(@id,"replies")]/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/ytd-continuation-item-renderer/tp-yt-paper-spinner'''.format(comment_no))

                if  len(spinner_loader)==0:
                    show_more_button = self.driver.find_elements(By.XPATH,replies_xpath+'/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/ytd-continuation-item-renderer')
                    if len(show_more_button) == 0:
                        show_more_button = None
                    break
                try:
                    if  spinner_loader[0].get_attribute("active") == "false":
                        show_more_button = self.driver.find_elements(By.XPATH,replies_xpath+'/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/ytd-continuation-item-renderer')
                        if len(show_more_button) == 0:
                            show_more_button = None
                        break
                except StaleElementReferenceException:
                    show_more_button = self.driver.find_elements(By.XPATH,replies_xpath+'/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/ytd-continuation-item-renderer')
                    if len(show_more_button) == 0:
                        show_more_button = None
                    break

            #collapse replies
        replies_content = self.driver.find_elements(By.XPATH,replies_xpath+'/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@id,"expander-contents")]/div[contains(@id,"contents")]/*')

        collapse_replies_button = self.driver.find_element(By.XPATH,replies_xpath+'/ytd-comment-replies-renderer/div[contains(@id,"expander")]/div[contains(@class,"expander-header")]/div[contains(@class,"less-button")]')
        self.driver.execute_script("arguments[0].scrollIntoView();", collapse_replies_button)
        # self.driver.execute_script("window.scrollBy(0, -100);")
        # collapse_replies_button.click()
        actions = ActionChains(self.driver)
        actions.move_to_element(collapse_replies_button)

        actions.click().perform()
        #   self.driver.execute_script("arguments[0].click();", collapse_replies_button)
        replies = []
        for r in replies_content:
            #   res=get_comment_data(r)
            res = self.__get_comment_data(r)
            replies.append(res)

        return replies


    def fetch_Comments(self):
        self.driver.set_window_size(1050, 708)
        self.driver.get(self.video_url)
        nav_bar= WebDriverWait(self.driver, self.element_wait_time).until(EC.visibility_of_element_located((By.XPATH,"/html/body/ytd-app/div[1]/div")))
        self.driver.execute_script("arguments[0].remove();",nav_bar)
        self.driver.execute_script("window.scrollBy(0, 500);")
        comments = []
        for i in range(2,self.commentNo+2):
            # print("reading comment no:", i)
            temp=[]
            comment_no = i
            comment_xpath ='''/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[{0}]/ytd-comment-renderer'''.format(comment_no)
            comment_section = WebDriverWait(self.driver, self.element_wait_time).until(EC.visibility_of_element_located((By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer')))
            self.driver.execute_script("arguments[0].scrollIntoView();", comment_section)
            try:
                comment = WebDriverWait(self.driver, self.element_wait_time).until(EC.visibility_of_element_located((By.XPATH,comment_xpath)))
            except TimeoutException:
                break
            # comment = self.driver.find_element(By.XPATH,comment_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", comment)
            comment = WebDriverWait(self.driver, self.element_wait_time).until(EC.visibility_of_element_located((By.XPATH,comment_xpath)))
            # self.driver.implicitly_wait()
            comment_data = self.__get_comment_data(comment)
            temp.append(comment_data)
            replies = self.__get_comment_replies(comment_no)
            temp.extend(replies)
            comments.append(temp)

        return comments