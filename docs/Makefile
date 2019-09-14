# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = src
BUILDDIR      = built

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# For the HTML build, must disable Jekyll (GH pages default formatter) for
# the custom theme to render freely and hence properly:
html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) "$(SOURCEDIR)" "$(BUILDDIR)"/html $(SPHINXOPTS) $(O)
	touch ./.nojekyll  # disable Jekyll to enable theming
	@echo
	@echo "Build finished."
	@echo "Open HTML index with 'firefox $(BUILDDIR)/html/index.html &'."
