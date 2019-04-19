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

if __name__ == "__main__":
    import pandas as pd
    from forecast import Forecaster
    games = pd.read_csv("https://raw.githubusercontent.com/crsmi/audl-elo/master/audl_elo.csv")

    def create_fran_lookup():
        return games.groupby('team_id').last()['fran_id'].to_dict()

    def create_elo_lookup():
        elos = games.groupby("fran_id")['elo_n'].last()
        return elos.to_dict()

    def create_forecaster(elo_lookup,fran_lookup):
        return Forecaster(elo_lookup,fran_lookup)

    def apply_forecaster(forecaster,teams):
        forecast = forecaster.forecast(teams[0],teams[1])
        return forecast

    elo_lookup = create_elo_lookup()
    fran_lookup = create_fran_lookup()
    f = create_forecaster(fran_lookup, elo_lookup)

    import pickle

    pickle.dump(f, open("audl_forecaster.pkl", "wb"))

    fprime = pickle.load(open("audl_forecaster.pkl", "rb"))

    print(apply_forecaster(fprime,['MAD','IND']))
