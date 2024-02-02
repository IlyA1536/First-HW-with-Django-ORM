import django_setup

from game_collection.models import Game, Genre

game1 = Game(
    name="game1",
    date_of_issue="2012-03-12",
    rating="2.5")
game1.save()

game2 = Game(
    name="game2",
    date_of_issue="2015-11-16",
    rating="3.2")
game2.save()

game3 = Game(
    name="game3",
    date_of_issue="2020-08-04",
    rating="4.1")
game3.save()

game4 = Game(
    name="game4",
    date_of_issue="2009-05-30",
    rating="4.6")
game4.save()

genre1 = Genre(
    genre = "Simulator"
)
genre1.save()

genre2 = Genre(
    genre = "Shooter"
)
genre2.save()
