python3 find_unique_matches.py report.md references.bib -e "@([\w_\-\d]+)" "@[\d\w]+\{([\w_\-\d]+),"

if [ $? -ne 0 ]; then
    echo "Warning: inconsistent references found"
    echo "$unique_refs"
fi

pandoc report.md -o report.pdf \
    --citeproc \
    --from markdown+inline_notes
echo "Compilation complete"