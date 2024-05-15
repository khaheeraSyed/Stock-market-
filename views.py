from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Watchlist, Stock
from .utils import fetch_stock_data

class WatchlistView(APIView):
    def get(self, request):
        user = request.user
        watchlist = Watchlist.objects.filter(user=user)
        symbols = [item.symbol for item in watchlist]
        stock_data = fetch_stock_data(symbols)
        return Response(stock_data)
      
