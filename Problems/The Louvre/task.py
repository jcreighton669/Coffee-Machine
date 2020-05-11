class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        print('"{}" by {} ({}) hangs in the Louvre.'.format(title, artist,
                                                            year))

title = input()
artist = input()
year = input()

my_painting = Painting(title, artist, year)
