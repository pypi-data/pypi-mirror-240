def swap_if_needed(a, b, need_one, need_two):
    if a.type == need_one and b.type == need_two:
        return a, b
    elif a.type == need_two and b.type == need_one:
        return b, a
    return


def line_orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def on_segment(p, q, r):
    if (max(p[0], r[0]) >= q[0] >= min(p[0], r[0]) and
            max(p[1], r[1]) >= q[1] >= min(p[1], r[1])):
        return True
    return False


def do_lines_intersect(line1, line2):
    p1, q1 = ((line1[0][0], line1[0][1]), (line1[0][2], line1[0][3]))
    p2, q2 = ((line2[0][0], line2[0][1]), (line2[0][2], line2[0][3]))

    o1 = line_orientation(p1, q1, p2)
    o2 = line_orientation(p1, q1, q2)
    o3 = line_orientation(p2, q2, p1)
    o4 = line_orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def distance_point_to_line(point, line):
    x0, y0 = point
    x1, y1, x2, y2 = line

    distance = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

    return distance


def does_line_intersect_pixel(line, pixel):
    distance = distance_point_to_line(pixel, line)

    return distance <= 0.5


def check_collision(obj_a, obj_b):
    if obj_a.type == "line" and obj_b.type == "line":
        return do_lines_intersect(obj_a.position, obj_b.position)
    swapped = swap_if_needed(obj_a, obj_b, "line", "pixel")
    if swapped[0].type == "line" and swapped[1].type == "pixel":
        return does_line_intersect_pixel(swapped[0].position, swapped[1].position)
