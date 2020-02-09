import uuid

class Exhibition(object):
  def __init__(self, title, description, image_url, languages, time, type, items, _id=None):
    if _id:
      self._id = _id
    else:
      self._id = str(uuid.uuid4())
    self.title = title
    self.description = description
    self.image_url = image_url
    self.languages = languages
    self.time = time
    self.type = type
    self.items = items

  @staticmethod
  def from_dict(source):
    exhibition = Exhibition(
      source[u'title'],
      source[u'description'],
      source[u'image_url'],
      source[u'languages'],
      source[u'time'],
      source[u'type'],
      source[u'items'],
      _id=source[u'_id']
    )
    return exhibition

  def to_dict(self):
    dest = {
      u'_id': self._id,
      u'title': self.title,
      u'description': self.description,
      u'image_url': self.image_url,
      u'languages': self.languages,
      u'time': self.time,
      u'type': self.type,
      u'items': self.items,
    }
    return dest

  def __repr__(self):
    return(
      u'Exhibition(id={}, title={}, description={}, image_url={}, languages={}, time={}, type={}, items={})'
      .format(self._id, self.title, self.description, self.image_url,
              self.languages, self.time, self.type, self.items))
