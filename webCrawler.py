import requests, bs4

# FUNCTIONALITY
'''
1) Accept an input
2) Match the input to one of the strings in self.topics
3) Navigate to the corresponding webpage
4) Navigate to workouts related to the requested topic
5) Extract exercise names, and navigate to the exercise page
6) Check the exercise level (beginner, intermediate, advanced)
7) Return the exercise if it corresponds to the requested level
8) Construct a workout
9) Return the workout to the caller
'''


class crawler:

    # Class variables
    topics = ['chest', 'shoulders', 'abs', 'back', 'biceps', 'tricep', 'legs']

    # Public methods, use externally
    def __init__(self):
        self.query = None
        self.url = 'https://www.bodybuilding.com/topic/'
        self.exerciseSet = set()

    def webSearch(self, query):
        # Match the given query to one of the available topics
        self.query = crawler.match_query(query=query)

        # Navigate to the requested topic page on www.bodybuilding.com
        self.url = self.url + self.query

        # Download the webpage for html parsing
        res = requests.get(self.url)
        res.raise_for_status()

        page = bs4.BeautifulSoup(res.text, features="html.parser")
        linkContainer = page.find("div", class_="cms-article-list--container")
        articles = linkContainer.find_all('span', class_='cms-article-list--article col col-1')

        workoutLinks = []

        for article in articles:
            articleType = article.find('figure').find('figcaption').find('span', class_='category').text

            if (articleType == 'Workouts'):
                workoutLinks.append(article.find('figure').find('a')['href'])

        for link in workoutLinks:
            try:
                self.findExercises(link)
            except:
                pass

        print(self.exerciseSet)
    # --------------------------------------------------------------------------

    # Class methods, do not use externally
    @classmethod
    def match_query(cls, query):
        query = query.lower()

        if query in cls.topics:
            return query
        else:
            raise Exception('Query could not be matched')

    def findExercises(self, link):
        # Download the page
        res = requests.get(link)
        res.raise_for_status()

        page = bs4.BeautifulSoup(res.text, features="html.parser")
        exerciseContainer = page.find('div', class_='cms-article-list__container cms-article__workout-plan bbcomWorkoutPlan')
        exerciseContainer = exerciseContainer.find('div', class_='cms-article-list__content--wrapper')
        exerciseContainer = exerciseContainer.find_all('div', class_='cms-article-list__content--container')

        for ex in exerciseContainer:
            exercise = ex.find('div',class_='cms-article-list__content').find('div')
            exercise = exercise.find('div',class_='cms-article-workout__exercise--info').find('a').text
            self.exerciseSet.add(exercise)
