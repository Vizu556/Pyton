import asyncio
import flet as ft


async def main(page: ft.Page)->None:
    page.title = "FruitC0in"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#7B68EE"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"Uni Sans Heavy": "fonts/Uni Sans Heavy.otf"}
    page.theme = ft.Theme(font_family="Uni Sans Heavy")


    
    

    async def score_up(event: ft.ContainerTapEvent)-> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95

        score_counter.opacity = 50
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = event.local_x
        score_counter.top = event.local_y
        score_counter.bottom = 0

        progress_bar.value += (1 / 100) # 0.1

        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="🪙 +100",
                    size=20,
                    color="#FFB6C1",
                    text_align=ft.TextAlign.CENTER,
                ),
                bgcolor="#BA55D3"
            )
            page.snack_bar.open = True
            progress_bar.value = 0

        await page.update_async()

        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0

        await page.update_async()



    image = ft.Image(
        src="Drop.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    score =ft.Text(value="0",size=100,data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="Fruit15.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,# 0-1
        width=page.width - 100,
        bar_height=20,
        color="#FF00FF",
        bgcolor="#6A5ACD"
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10 ,10, 10, 10)
        )
    )






if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)