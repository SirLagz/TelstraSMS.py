# TelstraSMS.py
A Python script to access Telstra SMS API - https://dev.telstra.com/sms-quick-start

This python script was designed to be used with Zabbix, however it's a generic script that can be used on the command line to send SMSes via the Telstra SMS API

Usage is telstrasms.py RECIPIENT MESSSAGE

Details on how I'm using it is available here - http://sirlagz.net/2015/06/15/using-the-telstra-sms-api-with-zabbix/

To get replies for the messages, use getReplies.py MESSAGEID

MESSAGEID is returned by telstrasms.py

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
