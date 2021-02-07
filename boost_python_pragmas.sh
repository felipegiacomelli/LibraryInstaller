# ./bootstrap.sh --with-libraries=python --prefix=/home/felipe/Libraries/boost-1.74.0/release/shared --with-python-version=3.9 --with-python=/usr/bin/python3 --with-python-root=/usr/include/python3.9
# ./bootstrap.sh --with-libraries=python --prefix=/home/felipe/Libraries/boost-1.74.0/release/shared --with-python-version=3.9 --with-python-root=/usr/include/python3.9
# ./b2 variant=release threading=multi --cxxflags=-fPIC link=shared runtime-link=shared --prefix=/home/felipe/Libraries/boost-1.74.0/release/shared -j 3 install
find $BOOST_DIR/release/shared/include/boost -type f -exec sed -i '/BOOST_HEADER_DEPRECATED(*/d' {} \;
sed -i '36,41d' $BOOST_DIR/release/shared/include/boost/bind.hpp
