var f = new File(Folder.userData + "/Adobe/Illustrator Script Runner/run_this.jsx");
if (f.exists) {
    $.evalFile(f);
}
