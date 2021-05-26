RELEASE ?= 0.0.1

all: rpm

clean:
	rm -rf src/test/__pycache__
	rm -rf src/carcano/ansibleinventory/__pycache__
	rm -rf src/bin/__pycache__
	rm -rf src/carcano_ansibleinventory.egg-info
	rm -rf src/dist
	rm -rf src/.eggs

unittests:
	cd src; python3 -m unittest discover -v

tarball: clean
	cd src; python3 setup.py sdist

rpm: tarball
	[ -d ~/rpmbuild ] || mkdir ~/rpmbuild
	[ -d ~/rpmbuild/SOURCES ] || mkdir ~/rpmbuild/SOURCES
	[ -d ~/rpmbuild/SPECS ] || mkdir ~/rpmbuild/SPECS
	mv src/dist/carcano_ansibleinventory-${RELEASE}.tar.gz ~/rpmbuild/SOURCES
	cp RPM/SPECS/carcano_ansibleinventory.spec ~/rpmbuild/SPECS
	cd ~/rpmbuild/SPECS; rpmbuild --define "_version ${RELEASE}" -ba carcano_ansibleinventory.spec
