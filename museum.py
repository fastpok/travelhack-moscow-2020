import uuid

from exhibition import Exhibition

class Museum(object):
  def __init__(self, title, image_url, latitude, longitude, exhibitions, _id=None):
    if _id:
      self._id = _id
    else:
      self._id = str(uuid.uuid4())
    self.title = title
    self.image_url = image_url
    self.latitude = latitude
    self.longitude = longitude
    self.exhibitions = exhibitions

  @staticmethod
  def from_dict(source):
    museum = Museum(
      source[u'title'],
      source[u'image_url'],
      source[u'latitude'],
      source[u'longitude'],
      [Exhibition.from_dict(x) for x in source[u'exhibitions']],
      _id=source[u'_id']
    )
    return museum

  def to_dict(self):
    dest = {
      u'_id': self._id,
      u'title': self.title,
      u'image_url': self.image_url,
      u'latitude': self.latitude,
      u'longitude': self.longitude,
      u'exhibitions': [Exhibition.to_dict(x) for x in self.exhibitions]
    }
    return dest

  def __repr__(self):
    return(
      u'Museum(id={}, title={}, image_url={}, latitude={}, longitude={}, exhibitions={})'
      .format(self._id, self.title, self.image_url, self.latitude,
              self.longitude, self.exhibitions))
