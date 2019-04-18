class Forecaster():
    def __init__(self,fran_lookup,elo_lookup):
        self._fran_lookup = fran_lookup
        self._elo_lookup = elo_lookup
        self._ELO_POINT_RATIO = 1/32
        self._HFA = 64

    def forecast(self,home_team,away_team):
        home_fran = self._fran_lookup[home_team]
        away_fran = self._fran_lookup[away_team]
        elo_diff = self._elo_lookup[home_fran] + self._HFA - self._elo_lookup[away_fran]
        forecast = 1/(1+(10**(-elo_diff/400)))
        return [forecast,1-forecast,elo_diff*self._ELO_POINT_RATIO]
