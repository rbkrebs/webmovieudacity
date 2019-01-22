# Movie Website

Movie Website is a project created during the Full Stack Web Developer Nanodegree Program from `Udacity`.
It has `three` python files:media.py, entertainment_center.py and fresh_tomatoes.py

## Configuration

To run this project, you must have installed in your computer the python 2. Follow the instructions
according to this [link](https://www.python.org/downloads/).
Both files must be into the same folder to run properly.
For downloading the files, please, check this repository [Github](https://github.com/rbkrebs/webmovieudacity.git)


The file `media.py` has the class `Movie()`. This class has two methods:

Its constructor, wich receive 4 parameter: the title of the movie, a short phrase about the movie, a link of the image
related to the movie and a youtube link with the trailer.
```
def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
```

The second one opens a web browser, using the webbrowser function `open()`. 
```
    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
```

The webbrowser is imported before class and you do not have to install, it is already in python 2. 
```
import webbrowser
```

The file `entertainment_center.py` has to import the `media.py` file and `fresh_tomatoes` file:
```
import media
import fresh_tomatoes
```

Then, you create a instance of `Movie()` class as follows:

```
kungfu_panda = media.Movie(
    "Drangon Warrior",
    "A panda is choosen to be the dragon warrior and save the village",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqfMwAq2qCQ6UcWsPRQlrQYvxfr4SNzrY8PjaOyt5prK14u3BGQw",
    "https://www.youtube.com/watch?v=AhbCYVILusc"
)
```
As you can see, there are 4 parameters: the title, a short phrase about the movie, a link to a picture and a link to the youtube trailer. You can create as many as you want, just changing the name of the instances and the parameters.

After all, you  create a list, like `movies` and add all the instances created.

```
movies = [kungfu_panda, dragao_branco, tropa_elite, marlei_eu]
```
This list will be the parameter of the function `open_movies_page(movies)`, that belongs to `fresh_tomatoes.py`file.
This file is responsable to create the `HTML` file according to the instances created before.

## Run

Once you have both files into the same folder (you can create a new forlder if you prefer),  run the entertainment_center.py file. This file has already some instances as examples. If you desire, you can add more follow the structure

## License

This project is under [MIT License](https://opensource.org/licenses/MIT)
