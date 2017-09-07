import media
import fresh_tomatoes

# create movie objects
finding_nemo = media.Movie("Finding Nemo",
    "https://lumiere-a.akamaihd.net/v1/images/uk_nem_mgp_classic_n_ac0e56bd.jpeg",  # NOQA
    "https://www.youtube.com/watch?v=wZdpNglLbt8")
despicable_me = media.Movie("Despicable Me",
    "https://images-na.ssl-images-amazon.com/images/I/51p%2BZw474tL.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zzCZ1W_CUoI")
frozen = media.Movie("Frozen",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-pkj97x_6b982198.jpeg?region=0%2C0%2C300%2C450",  # NOQA
    "https://www.youtube.com/watch?v=TbQm5doF_Uc")

# put movies into list
movies = [finding_nemo, despicable_me, frozen]

# generate html page
fresh_tomatoes.open_movies_page(movies)
