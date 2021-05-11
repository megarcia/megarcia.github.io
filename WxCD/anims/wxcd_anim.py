fname = 'wxcd_anim.html'
colors = ['white', 'yellow', 'red', 'blue', 'orange', 'purple']
with open(fname, 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<style>\n')
    f.write('.container {\n')
    f.write('  width: 900px;\n')
    f.write('  height: 600px;\n')
    f.write('  position: relative;\n')
    f.write('  background: white;\n')
    f.write('}\n')
    f.write('\n')
    f.write('.card {\n')
    f.write('    position: absolute;\n')
    f.write('    background-color: white;\n')
    f.write('    display: flex;\n')
    f.write('    align-items: center;\n')
    f.write('    text-align: center;\n')
    f.write('    justify-content: center;\n')
    f.write('    animation-duration: 60s;\n')
    f.write('    animation-timing-function: linear;\n')
    f.write('    animation-fill-mode: forwards;\n')
    f.write('}\n')
    f.write('\n')
    f.write('.grid {\n')
    f.write('    width: 32px;\n')
    f.write('    height: 20px;\n')
    f.write('    border: 1px solid black;\n')
    f.write('}\n')
    f.write('.collection {\n')
    f.write('    width: 30px;\n')
    f.write('    height: 22px;\n')
    f.write('    border: 2px solid black;\n')
    f.write('}\n')
    f.write('\n')
    start_top = 8
    for d in range(1, 21):
        left = 8
        cardname = 'wxcd_date%d_collection' % d
        animname = '%s_anim' % cardname
        top = start_top + 27 * (d - 1)
        f.write('.%s {\n' % cardname)
        f.write('    left: %dpx;\n' % left)
        f.write('    top: %dpx;\n' % top)
        f.write('    animation-name: %s;\n' % animname)
        f.write('}\n')
    f.write('\n')
    start_top = 10
    for d in range(1, 21):
        start_left = 10
        for v in range(1, 25):
            cardname = 'wxcd_date%d_var%d' % (d, v)
            animname = '%s_anim' % cardname
            left = start_left + 35 * (v - 1)
            top = start_top + 27 * (d - 1)
            f.write('.%s {\n' % cardname)
            f.write('    left: %dpx;\n' % left)
            f.write('    top: %dpx;\n' % top)
            f.write('    animation-name: %s;\n' % animname)
            f.write('}\n')
    f.write('\n')
    for d in range(1, 21):
        animname = 'wxcd_date%d_collection_anim' % d
        start_width = 34
        f.write('@keyframes %s {\n' % animname)
        f.write('    0%s   {width: %dpx;}\n' % ('%', start_width))
        for t in range(11, 15):
            width = start_width + 35 * (t - 11)
            f.write('    %d%s  {width: %dpx;}\n' % (t, '%', width))
        for t in range(d + 49, d + 70):
            width = start_width + 35 * (t - d - 46)
            f.write('    %d%s  {width: %dpx;}\n' % (t, '%', width))
        f.write('    100%s {width: %dpx;}\n' % ('%', width))
        f.write('}\n')
        for v in range(1, 5):
            animname = 'wxcd_date%d_var%d_anim' % (d, v)
            f.write('@keyframes %s {\n' % animname)
            f.write('    0%s   {background-color: white;}\n' % '%')
            f.write('    %d%s  {background-color: white;}\n' % ((v + 9), '%'))
            f.write('    %d%s  {background-color: %s;}\n' % ((v + 10), '%', colors[v]))
            f.write('    100%s {background-color: %s;}\n' % ('%', colors[v]))
            f.write('}\n')
        for v in range(5, 25):
            animname = 'wxcd_date%d_var%d_anim' % (d, v)
            f.write('@keyframes %s {\n' % animname)
            f.write('    0%s   {background-color: white;}\n' % '%')
            f.write('    %d%s  {background-color: white;}\n' % ((v + d + 44), '%'))
            f.write('    %d%s  {background-color: %s;}\n' % ((v + d + 45), '%', colors[-1]))
            f.write('    100%s {background-color: %s;}\n' % ('%', colors[-1]))
            f.write('}\n')
        f.write('\n')
    f.write('</style>\n')
    f.write('</head>\n')
    f.write('  <body>\n')
    f.write('    <h2>HTCondor "flood DAG" animated example</h2>\n')
    f.write('    <h3>sequential/rolling calculations with non-interfering file access</h3>\n')
    f.write('    <div class="container">\n')
    for d in range(1, 21):
        f.write('      <div class="animated card collection wxcd_date%d_collection"></div>\n' % d)
        for v in range(1, 25):
            f.write('      <div class="animated card grid wxcd_date%d_var%s"></div>\n' % (d, v))
    f.write('    </div>\n')
    f.write('  </body>\n')
    f.write('</html>\n')
