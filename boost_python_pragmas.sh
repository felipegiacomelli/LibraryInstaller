#!/bin/sh
# find $BOOST_DIR/release/shared/include/boost -type f -exec sed -i '/BOOST_HEADER_DEPRECATED(*/d' {} \;
# sed -i '36,41d' $BOOST_DIR/release/shared/include/boost/bind.hpp

find $BOOST_DIR/debug/shared/include/boost -type f -exec sed -i '/BOOST_HEADER_DEPRECATED(*/d' {} \;
sed -i '36,41d' $BOOST_DIR/debug/shared/include/boost/bind.hpp
