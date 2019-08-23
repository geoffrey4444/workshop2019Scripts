path_to_spec="/home/workshopStudents2019/spec/"
source ${path_to_spec}/MakefileRules/this_machine.env
echo "Collecting data for black hole horizons..."
${path_to_spec}/Support/bin/CombineSegments.py -o ./Vis -e h5 -f Horizons -L 2 -v 0
echo "Converting horizon data to format for movie making..."
cd ./Vis
${path_to_spec}/Support/bin/ConvertH5SurfaceToVtk ./ApparentHorizons/HorizonsDump.h5
cd ..
echo "Finished collecting black hole horizon data."
