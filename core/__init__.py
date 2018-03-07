# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CalculaVazao
                                 A QGIS plugin
 Plugin para Calculo de redes de esgotamento sanitario
                             -------------------
        begin                : 2016-03-15
        copyright            : (C) 2016 by Jorge Almerio
        email                : jorgealmerio@yahoo.com.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CalculaVazao class from file CalculaVazao.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from QEsg_00Settings import QEsg
    return QEsg(iface)
