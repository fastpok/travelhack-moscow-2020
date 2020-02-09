import uuid

class Item(object):
  def __init__(self, title, description, images, audio_files, author, ibeacon_uuid, ibeacon_major_id, ibeacon_minor_id, _id=None):
    if _id:
      self._id = _id
    else:
      self._id = str(uuid.uuid4())
    self.title = title
    self.description = description
    self.images = images
    self.audio_files = audio_files
    self.author = author
    self.ibeacon_uuid = ibeacon_uuid
    self.ibeacon_major_id = ibeacon_major_id
    self.ibeacon_minor_id = ibeacon_minor_id

  @staticmethod
  def from_dict(source):
    item = Item(
      source[u'title'],
      source[u'description'],
      source[u'images'],
      source[u'audio_files'],
      source[u'author'],
      source[u'ibeacon_uuid'],
      source[u'ibeacon_major_id'],
      source[u'ibeacon_minor_id'],
      _id=source[u'_id']
    )
    return item

  def to_dict(self):
    dest = {
      u'_id': self._id,
      u'title': self.title,
      u'description': self.description,
      u'images': self.images,
      u'audio_files': self.audio_files,
      u'author': self.author,
      u'ibeacon_uuid': self.ibeacon_uuid,
      u'ibeacon_major_id': self.ibeacon_major_id,
      u'ibeacon_minor_id': self.ibeacon_minor_id,
    }
    return dest

  def __repr__(self):
    return(
      u'Item(id={}, title={}, description={}, images={}, audio_files={}, author={}, ibeacon_uuid={}, ibeacon_major_id={}, ibeacon_minor_id={})'
      .format(self._id, self.title, self.description, self.images, self.audio_files,
              self.author, self.ibeacon_uuid, self.ibeacon_major_id, self.ibeacon_minor_id))
