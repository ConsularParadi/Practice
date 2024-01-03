from fastapi import FastAPI, Body
import flet as ft
import random
import schemas

# COLOR-SCHEME  
BG = '#041955'
FWG = '#97b4ff'
FG = '#3450a1'
PINK = '#eb06ff'

def main(page: ft.Page):

  page_1 = ft.Container(
    width=400,
    height=850,
    bgcolor=BG,
    border_radius=30,
    padding=ft.padding.only(top=60, left=50, right=200),
    content= ft.Column(
      controls=[
        ft.Container(
          on_click=lambda e: restore(e),
          content = ft.Icon(ft.icons.ARROW_BACK),
        ),
        ft.Container(
          content=profile_pic
        ),
        ft.Column(
          width = 150,
          height = 500,
          alignment = ft.alignment.center,
          controls = [
            ft.Container(height=30),
            ft.Text(value="Olivia\nMitchel", size=32, weight='bold', text_align=ft.TextAlign.LEFT),
            ft.Container(height=50),
            ft.Column(
              controls = [
                ft.Row(
                  controls= [
                  ft.Icon(ft.icons.STAR_OUTLINED),
                  ft.Text(value="\tImportant")
                  ]
                ),
                ft.Container(height=20),
                ft.Row(
                  controls= [
                  ft.Icon(ft.icons.TASK_OUTLINED),
                  ft.Text(value="\tCompleted Tasks")
                  ]
                ),
                ft.Container(height=20),
                ft.Row(
                  controls= [
                  ft.Icon(ft.icons.SHOPPING_BAG_OUTLINED),
                  ft.Text(value="\tCategories")
                  ]
                ),
                ft.Container(height=20),
                ft.Row(
                  controls= [
                  ft.Icon(ft.icons.SETTINGS_OUTLINED),
                  ft.Text(value="\tSettings")
                  ]
                ),
                ft.Container(height=20),
                ft.Row(
                  controls= [
                  ft.Icon(ft.icons.EXIT_TO_APP_OUTLINED),
                  ft.Text(value="\tLogout"),
                  ]
                )
              ]
            )
          ]
        )
      ]
    )
  )

  categories_card = ft.Row(
    scroll='auto',
  )
  categories = ['Family','Friends','Work','Personal','Others']
  for category in categories:
    categories_card.controls.append(
      ft.Container(
        bgcolor=BG,
        height=110,
        width=170,
        padding=15,
        border_radius=20,
        content = ft.Column(
          controls=[
            ft.Text(random.randint(1,10)),
            ft.Text(category),
            ft.Container(
              width=160,
              height=5,
              bgcolor='white12',
              border_radius=20,
              padding=ft.Padding(top=0, bottom=0, left=0, right=random.randint(10,100)),
              content=ft.Container(
                bgcolor=PINK,
              )
            )
          ]
        )
      )
    )
  
  tasks = ft.Column(
    height=400,
    scroll='auto',
  )

  tasks_list = [
    "Try to lick your elbow",
    "Do a silly dance for 30 seconds",
    "Talk in a fake accent for the next hour",
    "Try to do a handstand",
    "Sing your favorite song out loud",
    "Do a funny imitation of a celebrity",
    "Try to juggle 3 items",
    "Tell a funny joke",
    "Make a funny face and take a selfie",
    "Try to touch your nose with your tongue",
    "Do a cartwheel",
    "Try to write with your non-dominant hand",
    "Try to draw a picture with your eyes closed",
    "Try to do a magic trick",
    "Try to balance a spoon on your nose",
    "Try to say the alphabet backwards",
    "Try to do a push-up with your fingers",
    "Try to laugh without smiling",
    "Try to sneeze with your eyes open",
    "Try to do the worm dance move"
]

  for i in range(10):
    tasks.controls.append(
      ft.Container(
        height=70,
        width=400,
        bgcolor=BG,
        border_radius=20,
        padding=ft.Padding(top=10, bottom=0, left=0, right=50),
        content=ft.CupertinoCheckbox(
          value=False,
          label=tasks_list[i],
          active_color=PINK,
        )
      )
    )


  page_2_contents = ft.Container(
    content= ft.Column(
      controls=[
        ft.Row(
          alignment = 'spaceBetween',
          controls=[
            ft.Container(
              on_click=lambda e: shrink(e),
              content = ft.Icon(ft.icons.MENU)
            ),
            ft.Row(
              controls=[
                ft.Icon(ft.icons.SEARCH),
                ft.Icon(ft.icons.NOTIFICATIONS_ACTIVE_OUTLINED),
              ]
            )
          ]
        ),
        ft.Container(
          content = ft.Text(value="Let's get going, \nOlivia!", weight='bold', size=26),
          padding=ft.Padding(top=10, bottom=10, left=0, right=0),
        ),
        ft.Text(
          value="CATEGORIES",
        ),
        ft.Container(
          padding=ft.Padding(top=5, bottom=10, left=0, right=0),
          content = categories_card
        ),
        ft.Text("TODAY'S TASKS"),
        ft.Column(
          controls=[
            tasks,
          ]
        ),
        ft.Row(
          alignment = 'center',
          controls=[
            ft.FloatingActionButton(
              icon=ft.icons.ADD_OUTLINED,
              bgcolor=PINK,
              height=40,
              width=40,
              autofocus=True,
              on_click= lambda _: page.go("/create_task"),
              tooltip="Add Task",
            )
          ]
        )
      ]
    )
  )
  
  page_2 = ft.Row(
    alignment='end',
    controls=[
      ft.Container(
        width=400,
        height=850,
        bgcolor=FG,
        border_radius=30,
        animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
        animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
        padding=ft.Padding(
          top=50,left=20,right=20,bottom=5
        ),
        content= ft.Column(
          controls=[
            page_2_contents
          ]
        )
      )
    ]
  )

  container = ft.Container(
    width=400,
    height=850,
    bgcolor=BG,
    border_radius=30,
    content= ft.Stack(
      controls=[
        page_1,
        page_2
      ]
    )
  )
  
  create_task_view = ft.Container(
    content=ft.Container(
      height=40,width=40,
      content=ft.Icon(ft.icons.ARROW_BACK),
      on_click=lambda _: page.go('/')
    ),
  )

  page.add(container)

  pages = {
  '/': ft.View(
    "/",
    [container],
  ),
  '/create_task': ft.View(
    "/create_task",
    [create_task_view],
  )
  }

  def route_change(route):
    page.views.clear()
    page.views.append(
      pages[page.route]
    )
  
  def shrink(e):
    page_2.controls[0].width = 120
    page_2.controls[0].scale = ft.Scale(0.8, alignment=ft.alignment.center_right)
    page_2.controls[0].border_radius = ft.border_radius.only(
      top_left=35,
      top_right=0,
      bottom_left=35,
      bottom_right=0
    )
    page.update()

  def restore(e):
    page_2.controls[0].width = 400
    page_2.controls[0].scale = ft.Scale(1, alignment=ft.alignment.center_right)
    page.update()

  page.on_route_change = route_change
  page.go(page.route)


profile_pic = ft.Container(
  content=ft.Container(
      width=150,
      height=150,
      bgcolor=FG,
      border_radius=80,
      border=ft.border.all(color=PINK, width=5),
      content = ft.Container(
        width=100,
        height=100,
        bgcolor=BG,
        border_radius=80,
        border=ft.border.all(color=BG, width=5),
        content=ft.Image(
          src="https://picsum.photos/id/65/200",
          width=60,
          height=60,
          border_radius=80,
        )
      ),
    ),
)

ft.app(target=main, port=52420)
