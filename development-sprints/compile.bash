for num in 1 2 3 4 5; do
    pandoc "sprint-$num.md" -o "sprint-$num.pdf"
done
