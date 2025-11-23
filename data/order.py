from data.common import MainUrls


class InfoAboutOrder:
    URL_FOR_CREATE_ORDER = (f"{MainUrls.URL_STELLARBURGERS_API}/orders", "POST")
    NO_INGREDIENTS_ARE_INCLUDED_IN_THE_ORDER = {
        "success": False,
        "message": "Ingredient ids must be provided",
    }
