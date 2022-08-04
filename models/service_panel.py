from utils.db import db

class service_panel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    t_max = db.Column(db.Integer, nullable=False)
    t_min = db.Column(db.Integer, nullable=False)
    h_max = db.Column(db.Integer, nullable=False)
    h_min = db.Column(db.Integer, nullable=False)
    co2_min = db.Column(db.Integer, nullable=False)
    co2_max = db.Column(db.Integer, nullable=False)

    def __init__(self, tmax, tmin, hmax, hmin, co2max, co2min) -> None:
        self.t_max = tmax
        self.t_min = tmin
        self.h_max = hmax
        self.h_min = hmin
        self.co2_max = co2max
        self.co2_min = co2min

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(uid):
        return service_panel.query.filter_by(id=uid)

    def __repr__(self) -> str:
        return "<service-panel id={}>".format(self.id)