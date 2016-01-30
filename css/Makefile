SCSS_SCRIPTS = main.css

SCSSC = sass
SCSSCFLAGS =
STATIC = static

.SUFFIXES:
.SUFFIXES: .scss .css

all: clean build

build: $(SCSS_SCRIPTS)

clean:
	rm -fv $(SCSS_SCRIPTS)

.scss.css:
	$(SCSSC) $(SCSSCFLAGS) $< > $@

install: $(SCSS_SCRIPTS)
	cp -v $(SCSS_SCRIPTS) $(OUTPUT)/css/

.PHONY: build
