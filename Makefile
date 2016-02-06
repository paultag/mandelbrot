

build: coffee css


build:
	make -C coffee build
	make -C css build


.PHONY: build coffee css
