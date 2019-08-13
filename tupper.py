__author__ = 'antonio franco'

'''
Copyright (C) 2019  Antonio Franco (antonio_franco@live.it)
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
'''

import mpmath as mp
import matplotlib.pyplot as plt
import numpy as np
import os

mp.mp.dps = 1000  # increasing the precision of mpmath


class TupperPy(object):
    def __init__(self) -> None:
        """
        Represents the Tupper's original self-referential formula, that can be shifted up and down by multiples of 17
        """
        super().__init__()

        # Tupper's original number
        k_string = "960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350" \
                   "718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995" \
                   "165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183" \
                   "454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874" \
                   "46184837873723819822484986346503315941005497470059313833922649724946175154572836670236974546101" \
                   "4655997933798537483143786841806593422227898388722980000748404719"

        self.k = mp.mpmathify(k_string)

        # Height and width of a standard Tupper's bitmap
        self.height = 106
        self.width = 17

    @staticmethod
    def tupper(x: float, y: float) -> bool:
        """
        Calculates the Tupper's inequality in x and y
        :param x: horizontal shift
        :param y: vertical shift
        :return:
        """
        return 0.5 < mp.floor(mp.fmod(mp.floor(y / 17) * 2 ** (-17 * mp.floor(x) - mp.fmod(mp.floor(y), 17)), 2))

    def tupper_bmp(self, i: mp.mpf = 0) -> np.matrix:
        """
        Returns a bitmap representing the i-th shift from the Tupper's original self-referential formula
        :param i: i-th shift
        :return: boolean matrix representing the bitmap
        """
        bmp = mp.matrix(self.height, self.width)

        for x in mp.arange(self.height):
            for y in mp.arange(self.width):
                bmp[x, y] = TupperPy.tupper(x, (self.k + y + 17 * i))

        np_bmp = np.matrix(bmp.transpose().tolist(), dtype=bool)

        return np.flip(np_bmp, 1)

    def plot_tupper(self, i: mp.mpf = 0) -> None:
        """
        Creates a figure and plots a bitmap representing the i-th shift from the Tupper's original self-referential
         formula
        :param i:  i-th shift
        """
        plt.figure()

        bmp = self.tupper_bmp(i)

        plt.imshow(bmp, cmap='Greys', interpolation='nearest')

        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)


if __name__ == '__main__':
    # Creates two png's representing two vertical slices of the Tupper's formula
    T = TupperPy()

    # Classical Tupper's self-referential formula
    T.plot_tupper()
    plt.savefig(os.path.join("images", "tupper_classic.png"))

    # "Sick" k from http://keelyhill.github.io/tuppers-formula/
    k_sick = mp.mpf("19990658104895992159906328363638101787663851414537751539476865503218289618184076530123376594191"
                    "24042366024039498437918666302237803582546013046303926310513280468110193127095922276315009796499"
                    "31518795365589332244156816053373014059549452066117357397504861137579902513441094521287520230019"
                    "51866779239406656151423658961709308717100436684082889189269813403152930991277247967173513256539"
                    "22379772695517817049137311869862432577488386845165968713631941327344461868561513599475049479806"
                    "55286675865714081044922472071253")

    # Taking the difference divided by 17, and passing it to the method
    k_diff = (T.k - k_sick) / 17

    T.plot_tupper(-k_diff)
    plt.savefig(os.path.join("images", "tupper_sick.png"))
