import json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import download_dataset
class DownloadTests(unittest.TestCase):
    def test_default_registry_rejects_unapproved(self):
        with self.assertRaisesRegex(ValueError,"not approved"):
            download_dataset.download("echonet-dynamic")
    def test_unknown_rejected(self):
        with self.assertRaisesRegex(ValueError,"Unknown"):
            download_dataset.download("not-real")
    def test_no_portal_url_as_direct_download(self):
        with tempfile.TemporaryDirectory() as tmp:
            reg=Path(tmp)/"register.json"
            reg.write_text(json.dumps({"datasets":[{"id":"test","approved":True,"version":"v1","sha256":"a"*64}]}))
            with patch.object(download_dataset,"REG",reg):
                with self.assertRaisesRegex(ValueError,"direct approved HTTPS"):
                    download_dataset.download("test")
if __name__=="__main__":unittest.main()
