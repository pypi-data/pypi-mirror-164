# Making a udocker release

* Verify that the version is updated.
* Update the `CHANGELOG.md`.
* build python binary dist to upload to pypi

* Make an independent tarball of udocker

```bash
cd utils
./make_udockertar.sh
cd ..
```

* It produces udocker-x.y.z.tar.gz
* On github make a **new release** and upload this tarball, copy/paste text from other release.

