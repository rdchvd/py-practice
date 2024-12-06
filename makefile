.PHONY: new-task

new-task:
	python3 manage.py new-task $(task) -d $(dir)
