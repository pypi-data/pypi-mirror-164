import abc
import json
from pathlib import Path
from PIL import Image

from nonebot_plugin_PicMenu.img_tool import simple_text, multi_text, ImageFactory, auto_resize_text


class PicTemplate(metaclass=abc.ABCMeta):  # 模板类
    def __init__(self):
        pass

    @abc.abstractmethod
    def generate_main_menu(self, data, event) -> Image:
        """
        生成主菜单抽象方法
        :param data:
        :param event:
        :return:
        """
        pass


class DefaultTemplate(PicTemplate):
    def __init__(self):
        super().__init__()
        self.name = 'default'
        self.load_resource()
        self.colors = {
            'blue': (23, 43, 59),
            'yellow': (224, 164, 25),
            'white': (237, 239, 241)
        }
        self.basic_font_size = 25
        self.current_week = None

    def load_resource(self):
        cwd = Path.cwd()
        with (cwd / 'data' / 'course_config' / 'config.json').open('r', encoding='utf-8') as fp:
            config = json.load(fp)
        self.using_font = config['default']

    def generate_main_menu(self, data: dict, event, current_week=None) -> Image:
        user_id = event.user_id

        # 列数
        column_num = 8

        # 行数
        row_num = 13

        # 数据及表头尺寸测算
        row_size_list = [[[300, 0]for _ in range(row_num + 1)] for _ in range(column_num + 1)]

        # 计算周一至周日课表的尺寸
        row_max = -1
        for x in range(7):
            if x == 0:
                continue
            for y in range(13):
                if y == 0:
                    continue
                x = str(x)
                y = str(y)
                info = ""
                for course in data[x][y]:
                    if current_week is not None and current_week not in course['week']:
                        continue
                    else:
                        info += f"""{course["name"]}\n{course["teacher"]}\n{course["classroom"]}"""
                course_info_size = multi_text(info,
                                              default_font=self.using_font,
                                              default_size=25,
                                              box_size=(215, 0)
                                              ).size
                # 行高度计算
                x = int(x)
                y = int(y)
                row_size_list[x][y][1] = course_info_size[1]
                row_max = max(row_max, course_info_size[1])

        # 单元格边距
        margin = 10

        # 确定每行的行高
        row_height_list = row_max + margin * 2

        # 确定每列的列宽
        column_width_list = 225

        # 确定表格底版的长和宽
        table_width = (160 + margin) * 10 + 3 + margin * 12
        table_height = 14 * row_height_list + 3

        # 新建白板图片
        table = ImageFactory(
            Image.new('RGBA', (table_width, table_height), self.colors['white'])
        )

        # 绘制基点和移动锚点
        initial_point, basis_point = (1, 1), [1, 1]

        # 为单元格添加box和绘制边框
        for row_id in range(row_num + 1):
            for col_id in range(column_num):
                box_size = (column_width_list, row_height_list)
                table.add_box(f'box_{row_id}_{col_id}',
                              tuple(basis_point),
                              tuple(box_size))
                table.rectangle(f'box_{row_id}_{col_id}', outline=self.colors['blue'], width=2)
                basis_point[0] += box_size[0]
            basis_point[0] = initial_point[0]
            basis_point[1] += row_height_list

        # 向单元格中填字
        for i, text in enumerate(('上课时间', '周一', '周二', '周三', '周四', '周五', '周六', '周日')):
            header = simple_text(text, self.basic_font_size, self.using_font, self.colors['blue'])
            table.img_paste(
                header,
                table.align_box(f'box_0_{i}', header, align='center'),
                isalpha=True
            )
        exact_time = {
            "1": {"start": "08:20", "end": "09:05"},
            "2": {"start": "09:10", "end": "09:55"},
            "3": {"start": "10:15", "end": "11:00"},
            "4": {"start": "11:05", "end": "11:50"},
            "5": {"start": "11:55", "end": "12:25"},
            "6": {"start": "12:30", "end": "13:00"},
            "7": {"start": "13:10", "end": "13:55"},
            "8": {"start": "14:00", "end": "14:45"},
            "9": {"start": "15:05", "end": "15:50"},
            "10": {"start": "15:55", "end": "16:40"},
            "11": {"start": "18:00", "end": "18:45"},
            "12": {"start": "18:50", "end": "19:35"},
            "13": {"start": "19:40", "end": "20:25"},
        }
        for x in range(row_num):
            row_id = x + 1
            id_text = simple_text(f"{exact_time[str(row_id)]['start']} - {exact_time[str(row_id)]['end']}",
                                  self.basic_font_size, self.using_font, self.colors['blue'])
            table.img_paste(
                id_text,
                table.align_box(f'box_{row_id}_0', id_text, align='center'),
                isalpha=True
            )
        for x in range(column_num):
            if x == 0:
                continue
            for y in range(row_num):
                if y == 0:
                    continue
                info = ""
                x = str(x)
                y = str(y)
                try:
                    for course in data[x][y]:
                        if current_week is not None and current_week not in course['week']:
                            continue
                        else:
                            info += f"""{course["name"]}\n{course["teacher"]}\n{course["classroom"]}"""
                    plugin_name_text = multi_text(info,
                                                  box_size=(215, 0),
                                                  default_font=self.using_font,
                                                  default_color=self.colors['blue'],
                                                  default_size=self.basic_font_size
                                                  )
                    table.img_paste(
                        plugin_name_text,
                        table.align_box(f'box_{y}_{x}', plugin_name_text, align='center'),
                        isalpha=True
                    )
                except KeyError:
                    pass
        table_size = table.img.size
        # 添加注释

        note_basic_text = simple_text('注：没显示就是没有你的数据，请联系管理员',
                                      size=self.basic_font_size,
                                      color=self.colors['blue'],
                                      font=self.using_font)
        msg = ""
        if current_week is not None:
            msg = f"当前周数：{current_week}"
        note_text = multi_text(msg,
                               box_size=(table_size[0] - 30 - note_basic_text.size[0] - 10, 0),
                               default_font=self.using_font,
                               default_color=self.colors['blue'],
                               default_size=self.basic_font_size,
                               spacing=4,
                               horizontal_align="middle"
                               )
        note_img = ImageFactory(
            Image.new('RGBA',
                      (note_text.size[0] + 10 + note_basic_text.size[0],
                       max((note_text.size[1], note_basic_text.size[1]))),
                      self.colors['white'])
        )
        note_img.img_paste(note_basic_text, (0, 0), isalpha=True)
        note_img.img_paste(note_text, (note_basic_text.size[0] + 10, 0), isalpha=True)
        main_menu = ImageFactory(
            Image.new('RGBA',
                      (table_size[0] + 140, table_size[1] + note_img.img.size[1] + 210),
                      color=self.colors['white'])
        )
        main_menu.img_paste(
            note_img.img,
            main_menu.align_box('self', table.img, pos=(0, 140), align='horizontal')
        )
        main_menu.img_paste(
            table.img,
            main_menu.align_box('self', table.img, pos=(0, 160 + note_img.img.size[1]), align='horizontal')
        )
        main_menu.add_box('border_box',
                          main_menu.align_box('self',
                                              (table_size[0] + 40, table_size[1] + note_img.img.size[1] + 80),
                                              pos=(0, 100),
                                              align='horizontal'),
                          (table_size[0] + 40, table_size[1] + note_img.img.size[1] + 90))
        main_menu.rectangle('border_box', outline=self.colors['blue'], width=5)
        border_box_top_left = main_menu.boxes['border_box'].topLeft
        main_menu.add_box('title_box', (0, 0), (main_menu.get_size()[0], 100))
        title = auto_resize_text(f"{user_id}的课表", 60, self.using_font, (table_width-60, 66), self.colors['blue'])
        main_menu.img_paste(title, main_menu.align_box('title_box', title, align='center'), isalpha=True)
        return main_menu.img
