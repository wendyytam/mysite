import course
import song

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='Snap',
                  resource_url='https://snap.berkeley.edu/'),
    course.Course(period=2,
                  name='AP English Literature and Composition',
                  teacher_name='Ms. Wilson',
                  resource_name='Capstone Blogs',
                  resource_url='https://2wendyt2018.blogspot.com/'),
    course.Course(period=3,
                  name='AP Calculus AB',
                  teacher_name='Mr. Wai',
                  resource_name='Calculus Textbook',
                  resource_url='http://hsebooks.kendallhunt.com/calc_se/ebook/kh.html'),
    course.Course(period=4,
                  name='Student Leadership',
                  teacher_name='Ms. Nelson',
                  resource_name='CADA',
                  resource_url='https://secure.cada1.org/i4a/pages/index.cfm?pageid=3461'),
    course.Course(period=5,
                  name='American Government',
                  teacher_name='Mr. Kelly',
                  resource_name='The Constitution',
                  resource_url='https://www.whitehouse.gov/about-the-white-house/the-constitution/'),
    course.Course(period=6,
                  name='Teacher Aide',
                  teacher_name='Ms. Belli',
                  resource_name='FAFSA',
                  resource_url='https://fafsa.ed.gov/')
]

TOP_TEN_SONGS = [
    song.Song(title='Small Bump',
                artist_name='Ed Sheeran',
                youtube_url='https://www.youtube.com/watch?v=A_af256mnTE'),
    song.Song(title='The Middle',
                artist_name='Zedd,Grey ft. Marren Morris',
                youtube_url='https://www.youtube.com/watch?v=xQzS3JnZQZM'),
    song.Song(title='Tonight',
                atist_name='Kidswaste & Manila Killa',
                youtube_url='https://www.youtube.com/watch?v=CM_FUei7klk'),
    song.Song(title='I Want It That Way',
                artist_name='Backstreet Boys',
                youtube_url='https://www.youtube.com/watch?v=4fndeDfaWCg'),
    song.Song(title='Waves',
                artist_name='Dean Lewis'
                youtube_url='https://www.youtube.com/watch?v=KAM1wyQJsto'),
    song.Song(title='Stargazing',
                artist_name='Kygo',
                youtube_url='https://www.youtube.com/watch?v=hEdvvTF5js4&list=PLP6DbdnAphCWRmweqvT6XLLFX8jCZrzfb&index=6'),
    song.Song(title='Finesse',
                artist_name='Bruno Mars',
                youtube_url='https://www.youtube.com/watch?v=LsoLEjrDogU'),
    song.Song(title='Photograph',
                artist_name='Ed Sheeran',
                youtube_url='https://www.youtube.com/watch?v=nSDgHBxUbVQ'),
    song.Song(title='Miss Independent',
                artist_name='Ne-Yo',
                youtube_url='https://www.youtube.com/watch?v=k6M5C-oKw9k&list=PLZqfys784zTBG-a1JtJUQLDVNQ95WkiOp'),
    song.Song(title='Knock You Down',
                artist_name='Keri Hilson ft. Kanye West, Ne-Yo',
                youtube_url='https://www.youtube.com/watch?v=p_RqWocthcc')
]



