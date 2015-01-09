Company Subdivision Report Module
#################################

The company subdivision report module manage reports to printer in company subdivisions.

Configuration
=============

Add reports and directories related in each company subdivision (you could manage in
company subdivision or in reports).

This module have a new method (report_directory) to get directory name according to action report and subdivision.

Reports
=======

In your module, rewrite "execute" method report class and call "report_directory" method.

A design in execute method is:
* If report have a directory configured and current user in their preferences have a subvision,
  when execute report is writed in the directory (with extension).
* Finally, if report have direct print, not return report to client.

Extra configuration
===================

Configure a watchdirectory to print automatlly reports to printers.
