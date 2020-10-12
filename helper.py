#!/usr/bin/env python3
import sqlite3 as lite

DB_PATH='./todo_db_files/todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
	try:
		conn = lite.connect(DB_PATH)

		# Once a connection has been established, we use the cursor
        	# object to execute queries
		cur = conn.cursor()
		
		# Keep the initial status as Not Started
		cur.execute('insert or replace into items(item, status) values(?,?)', (item, NOTSTARTED))

		conn.commit()
		return {"item": item, "status": NOTSTARTED}

	except Exception as e:
		print('Error: ', e)
		return None	

def get_all_items():
	try:
		conn = lite.connect(DB_PATH)
		cur = conn.cursor()
		cur.execute('select * from items')
		rows = cur.fetchall()
		return { "count": len(rows), "items": rows }

	except Exception as e:
		print('Error', e)
		return None

def get_item(item):
        try:
                conn = lite.connect(DB_PATH)
                cur = conn.cursor()
                cur.execute("select status from items where item='%s'" % item)
                status = cur.fetchone()[0]
                return status

        except Exception as e:
                print('Error: ', e)
                return None

def update_status(item, status):
	# Check if the passed status is a valid value
	if status.lower().strip() == 'not started':
		status = NOTSTARTED
	elif status.lower().strip() == 'in progress':
		status = INPROGRESS
	elif status.lower().strip() == 'completed':
		status = COMPLETED
	else:
		print("Invalid Status: " + status)
		return None
	
	try:
		conn = lite.connect(DB_PATH)
                cur = conn.cursor()
		cur.execute('update items set status=? where item=?', (status, item))
		conn.commit()
		return {item: status}
	except Exception as e:
		print('Error: ', e)
        	return None 

def delete_item(item):
    try:
        conn = lite.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where item=?', (item,))
        conn.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None

