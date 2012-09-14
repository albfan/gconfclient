import gconf

class AbstractGConfViewer:
    """ """
    def __init__(self, dirkey):
        self.dirkey = dirkey

        client = gconf.client_get_default()
        client.add_dir(self.dirkey + "/custom0", gconf.CLIENT_PRELOAD_NONE)
        client.notify_add(self.dirkey + '/custom0/name', self.on_key_changed)

    def on_key_changed(self, client, *args, **kwargs):
        keyName = self.getKeyName()
        value = client.get_string(self.dirkey + '/custom0/' + keyName)
        result = keyName + " = " + value + "\n"
        self.setResult(result)